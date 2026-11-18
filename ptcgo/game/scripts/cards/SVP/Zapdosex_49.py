from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5bdfc08f-7be9-5c01-8d5d-ee8ae92b2516",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zapdosex.Name",
    display_name="Zapdos ex",
    searchable_by=["Zapdos ex", "Basic", "ex", "Zapdosex"],
    subtypes=["Basic", "ex"],
    collector_number=49,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=145,
    abilities=[
        Ability(
            title="Voltaic Float",
            game_text="If this Pok\u00e9mon has any Lightning Energy attached, it has no Retreat Cost.",
            effect=unimplemented,
        ),
        Attack(
            title="Multishot Lightning",
            game_text="This attack also does 90 damage to 1 of your opponent's Benched Pok\u00e9mon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=120,
            effect=unimplemented,
        ),
    ],
)