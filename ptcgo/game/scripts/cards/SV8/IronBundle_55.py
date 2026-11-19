from ptcgo.game.card_effects.attacks_common import damage_reduction_on_self, damage_counters_on, count_retreat_cost
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID

card = PokemonCardDef(
    guid="0e42bde2-d517-5340-bd07-62cd4a1cf04a",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronBundle.Name",
    display_name="Iron Bundle",
    searchable_by=["Iron Bundle", "Basic", "Future", "IronBundle"],
    subtypes=["Basic", "Future"],
    collector_number=55,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=991,
    abilities=[
        Attack(
            title="Gusting Collision",
            game_text="This attack does 50 less damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            damage_operator="-",
            effect=damage_reduction_on_self(per=50, count_fn=count_retreat_cost("defender")),
        ),
    ],
)