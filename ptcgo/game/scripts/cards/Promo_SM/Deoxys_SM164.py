from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import move_energy_between

def _is_deoxys(pokemon, ctx=None):
    from ptcgo.game.data_utils import def_for
    return (getattr(def_for(pokemon.archetype_id), "display_name", "") or "").startswith("Deoxys")


async def power_suction(ctx):
    """Move 1 Energy from one of your Pokemon to one of your Deoxys."""
    await move_energy_between(count=1, from_pool="any", to_pool="any",
                              to_pred=_is_deoxys,
                              prompt="Choose an Energy to move to a Deoxys")(ctx)


card = PokemonCardDef(
    guid="c8af6223-78de-5f42-82c1-94e23bad39da",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name",
    display_name="Deoxys",
    searchable_by=["Deoxys", "Basic", "Deoxys"],
    subtypes=["Basic"],
    collector_number=164,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=386,
    abilities=[
        Ability(
            title="Power Suction",
            game_text="Once during your turn (before your attack), you may move an Energy from 1 of your Pok\u00e9mon to 1 of your Deoxys.",
            activation=Activations.ONCE_PER_TURN,
            effect=power_suction,
        ),
        Attack(
            title="Psycho Boost",
            game_text="During your next turn, this Pok\u00e9mon's Psycho Boost attack's base damage is 50.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=unimplemented,
        ),
    ],
)