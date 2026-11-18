from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="38dc39e8-48d4-5e70-8a49-3f3eb9714f46",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raikou.Name",
    display_name="Raikou",
    searchable_by=["Raikou", "Basic", "Raikou"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="COL",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=243,
    abilities=[
        Ability(
            title="Extreme Speed",
            game_text="Raikou's Retreat Cost is Colorless less for each Lightning Energy attached to Raikou.",
            effect=unimplemented,
        ),
        Attack(
            title="Raging Thunder",
            game_text="Does 20 damage to 1 of your Pok\u00e9mon and don't apply Weakness and Resistance to this damage.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=unimplemented,
        ),
    ],
)