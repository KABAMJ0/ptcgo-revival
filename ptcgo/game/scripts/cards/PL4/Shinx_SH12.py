from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="038df5dd-3430-59b8-92f0-1f074e5c536e",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shinx.Name",
    display_name="Shinx",
    searchable_by=["Shinx", "Basic", "Shinx"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="PL4",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=403,
    abilities=[
        Ability(
            title="Star Barrier",
            game_text="As long as Shinx has any Energy attached to it, Shinx has no Weakness.",
            effect=unimplemented,
        ),
        Attack(
            title="Payback",
            game_text="If your opponent has only 1 Prize card left, this attack does 10 damage plus 30 more damage.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)