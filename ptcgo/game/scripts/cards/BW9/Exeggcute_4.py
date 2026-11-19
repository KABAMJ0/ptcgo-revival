from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, \
    Activations, def_for
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import has_tool
from ptcgo.game.session.passives import ability_locked


def _garbotoxin_on_board(board) -> bool:
    """A Garbodor with a Tool and a scripted Garbotoxin switches off every
    Ability outside its own -- including one used from the discard pile, which
    the engine's in-play ability lock cannot reach."""
    for player_id in board.player_ids:
        for pokemon in board.pokemon_in_play(player_id):
            if not has_tool(pokemon):
                continue
            for entry in getattr(def_for(pokemon.archetype_id), "abilities", None) or []:
                if getattr(entry, "title", "") == "Garbotoxin" and \
                        getattr(entry, "passive", None) is not None and \
                        not ability_locked(board, pokemon):
                    return True
    return False


def propagation_condition(board, player_id, pokemon) -> bool:
    return not _garbotoxin_on_board(board)


async def propagation(ctx):
    """From the discard pile: put this Pokemon into your hand."""
    await ctx.put_in_hand([ctx.source], reveal=False)

card = PokemonCardDef(
    guid="5539136b-dc3d-5c73-a2b5-a7ca95f8b8e7",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    display_name="Exeggcute",
    searchable_by=["Exeggcute", "Basic", "Exeggcute"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    hp=30,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=102,
    abilities=[
        Ability(
            title="Propagation",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is in your discard pile, you may put this Pok\u00e9mon into your hand.",
            activation=Activations.ONCE_PER_TURN,
            usable_from="discard",
            condition=propagation_condition,
            effect=propagation,
        ),
        Attack(
            title="Seed Bomb",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)