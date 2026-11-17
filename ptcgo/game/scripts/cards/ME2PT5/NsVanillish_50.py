from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5e17ffc1-d6d5-5291-8082-17c6e4ad648a",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsVanillish.Name",
    display_name="N's Vanillish",
    searchable_by=["N's Vanillish", "Stage 1", "NsVanillish"],
    subtypes=["Stage 1"],
    collector_number=50,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.NsVanillite.Name",
    family_id=582,
    abilities=[
        Attack(
            title="Flop",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Sheer Cold",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't use attacks.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
    ],
)