from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cf1e90d9-7c9b-5531-88b2-5abd15e500a8",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninjask.Name",
    display_name="Ninjask",
    searchable_by=["Ninjask", "Stage 1", "Ninjask"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="EX8",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    family_id=290,
    abilities=[
        Ability(
            title="Fast Protection",
            game_text="Prevent all effects, including damage, done to Ninjask by your opponent's attacks from his or her Basic Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Swords Dance",
            game_text="During your next turn, Ninjask's Slash attack's base damage is 80.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)