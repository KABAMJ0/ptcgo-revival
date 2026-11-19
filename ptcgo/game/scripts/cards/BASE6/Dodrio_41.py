from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.passives_common import is_in_active_spot, retreat_discount
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _own_active_while_benched(pokemon, carrier):
    return (pokemon.owning_player_id == carrier.owning_player_id
            and is_in_active_spot(pokemon)
            and not is_in_active_spot(carrier))


card = PokemonCardDef(
    guid="c2c0f5ff-8206-5124-bab2-f1911b9d145d",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dodrio.Name",
    display_name="Dodrio",
    searchable_by=["Dodrio", "Stage 1", "Dodrio"],
    subtypes=["Stage 1"],
    collector_number=41,
    set_code="BASE6",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Doduo.Name",
    family_id=84,
    abilities=[
        Ability(
            title="Retreat Aid",
            game_text="As long as Dodrio is Benched, pay Colorless less to retreat your Active Pok\u00e9mon.",
            passive=retreat_discount(1, target_pred=_own_active_while_benched),
        ),
        Attack(
            title="Rage",
            game_text="Does 10 damage plus 10 more damage for each damage counter on Dodrio.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)