from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.session.passives import effective_max_hp
from ptcgo.game.content.definitions import Activations
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


def _water_targets(ctx):
    return [pokemon for pokemon in ctx.my_pokemon_in_play()
            if pokemon.get_attribute(AttrID.HP, 0) < ctx.max_hp(pokemon)
            and any(energy_provides_type(energy, PokemonTypes.WATER.value)
                    for energy in ctx.attached_energies(pokemon))]


def blessings_condition(board, player_id, pokemon):
    return any(
        p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)
        and any(energy_provides_type(energy, PokemonTypes.WATER.value)
                for energy in board.attached_energies(p))
        for p in board.pokemon_in_play(player_id)
    )


async def blessings_of_the_deep(ctx):
    candidates = _water_targets(ctx)
    if not candidates:
        return 0
    target = candidates[0] if len(candidates) == 1 else await ctx.choose_pokemon(
        candidates, "Choose a Pokémon with Water Energy to heal")
    if target is None:
        return 0
    return await ctx.heal(20, target)

card = PokemonCardDef(
    guid="c0724aab-3868-52c0-9ac9-f5730d22f50d",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manaphy.Name",
    display_name="Manaphy",
    searchable_by=["Manaphy", "Basic", "Manaphy"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="SL",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=490,
    abilities=[
        Ability(
            title="Blessings of the Deep",
            game_text="Once during your turn (before your attack), you may heal 20 damage from 1 of your Pok\u00e9mon that has any Water Energy attached to it.",
            activation=Activations.ONCE_PER_TURN,
            condition=blessings_condition,
            effect=blessings_of_the_deep,
        ),
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)