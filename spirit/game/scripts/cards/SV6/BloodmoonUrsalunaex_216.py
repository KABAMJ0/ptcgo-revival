from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="51953cab-21b8-5577-bbe0-2624582bec20",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BloodmoonUrsalunaex.Name",
    display_name="Bloodmoon Ursaluna ex",
    searchable_by=["Bloodmoon Ursaluna ex", "Basic", "ex", "BloodmoonUrsalunaex"],
    subtypes=["Basic", "ex"],
    collector_number=216,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=901,
    abilities=[
        Ability(
            title="Seasoned Skill",
            game_text="Blood Moon used by this Pok\u00e9mon costs Colorless less for each Prize card your opponent has taken.",
            effect=unimplemented,
        ),
        Attack(
            title="Blood Moon",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.COLORLESS: 5},
            damage=240,
            effect=unimplemented,
        ),
    ],
)