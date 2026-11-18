from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ee9efad5-3279-5e7e-add5-655837d5a835",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crawdauntex.Name",
    display_name="Crawdaunt ex",
    searchable_by=["Crawdaunt ex", "Stage 1", "ex", "Crawdauntex"],
    subtypes=["Stage 1", "ex"],
    collector_number=99,
    set_code="EX13",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Corphish.Name",
    family_id=341,
    abilities=[
        Ability(
            title="Splash Back",
            game_text="Once during your turn (before your attack), if your opponent has 4 or more Benched Pok\u00e9mon, you may choose 1 of them and return that Pok\u00e9mon and all cards attached to it to his or her hand. This power can't be used if Crawdaunt ex is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Power Blow",
            game_text="Does 20 damage times the amount of Energy attached to Crawdaunt ex.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)