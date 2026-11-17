from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c045a79c-4829-502d-b82b-f47b9d251ee0",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasVictreebel.Name",
    display_name="Erika's Victreebel",
    searchable_by=["Erika's Victreebel", "Stage 2", "ErikasVictreebel"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasWeepinbell.Name",
    family_id=69,
    abilities=[
        Attack(
            title="Flower Garden Rondo",
            game_text="This attack does 40 damage for each of your Erika's Pok\u00e9mon in play.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Solar Beam",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)