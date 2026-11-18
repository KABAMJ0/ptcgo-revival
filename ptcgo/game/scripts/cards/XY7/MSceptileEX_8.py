from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="078d89f2-1516-55b6-b58f-b08a3f9153d5",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MSceptileEX.Name",
    display_name="M Sceptile-EX",
    searchable_by=["M Sceptile-EX", "MEGA", "EX", "MSceptileEX"],
    subtypes=["MEGA", "EX"],
    collector_number=8,
    set_code="XY7",
    rarity=Rarities.RareHolo,
    hp=220,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SceptileEX.Name",
    family_id=254,
    abilities=[
        Attack(
            title="Jagged Saber",
            game_text="You may attach up to 2 Grass Energy cards from your hand to your Benched Pok\u00e9mon in any way you like. If you attached Energy to a Pok\u00e9mon in this way, heal all damage from that Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=unimplemented,
        ),
    ],
)