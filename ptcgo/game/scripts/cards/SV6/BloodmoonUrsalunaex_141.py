from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f6ec5fc2-5e7f-5c16-aedd-dcf51f537b1c",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BloodmoonUrsalunaex.Name",
    display_name="Bloodmoon Ursaluna ex",
    searchable_by=["Bloodmoon Ursaluna ex", "Basic", "ex", "BloodmoonUrsalunaex"],
    subtypes=["Basic", "ex"],
    collector_number=141,
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