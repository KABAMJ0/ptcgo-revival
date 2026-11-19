from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.passives_common import is_in_active_spot, retreat_free_when
from ptcgo.game.attributes import AttrID


def _tailwind_available(board, player_id, pokemon):
    return not is_in_active_spot(pokemon) and not pokemon.get_attribute(
        AttrID.SPECIAL_CONDITIONS) and board.active_pokemon(player_id) is not None


async def _tailwind(ctx):
    active = ctx.my_active()
    if active is None:
        return
    ctx.add_temporary_passive(
        active, retreat_free_when(lambda pokemon, carrier: pokemon is active),
        expires_after_turn=ctx.session.turn_state.turn_number)


card = PokemonCardDef(
    guid="f9d08e6c-bf52-5515-9d41-925536228fd0",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonite.Name",
    display_name="Dragonite",
    searchable_by=["Dragonite", "Stage 2", "Dragonite"],
    subtypes=["Stage 2"],
    collector_number=9,
    set_code="ECARD1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    family_id=147,
    abilities=[
        Ability(
            title="Tailwind",
            game_text="Once during your turn (before your attack), if Dragonite is on your Bench, you may reduce your Active Pok\u00e9mon's Retreat Cost to 0.",
            activation=Activations.ONCE_PER_TURN,
            condition=_tailwind_available,
            effect=_tailwind,
        ),
        Attack(
            title="Dragon Tail",
            game_text="Flip 2 coins. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1},
            damage=40,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=40),
        ),
    ],
)