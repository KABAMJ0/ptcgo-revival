from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="079af3bf-5083-57e8-b546-f833686f91bf",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zapdosex.Name",
    display_name="Zapdos ex",
    searchable_by=["Zapdos ex", "Basic", "ex", "Zapdosex"],
    subtypes=["Basic", "ex"],
    collector_number=145,
    set_code="SV3PT5",
    rarity=Rarities.Rare,
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