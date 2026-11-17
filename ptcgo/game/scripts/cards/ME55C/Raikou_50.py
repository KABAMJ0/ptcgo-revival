from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7037b449-b22b-5f02-9118-0b359dcf2ddf",
    key="ME55C",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raikou.Name",
    display_name="Raikou",
    searchable_by=["Raikou", "Basic", "Raikou"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="ME55C",
    rarity=Rarities.Amazing,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=243,
    abilities=[
        Attack(
            title="Amazing Shot",
            game_text="This attack also does 120 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.METAL: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)