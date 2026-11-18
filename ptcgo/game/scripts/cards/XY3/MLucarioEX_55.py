from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="263409b1-6d43-516e-ae53-7897dfe21127",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MLucarioEX.Name",
    display_name="M Lucario-EX",
    searchable_by=["M Lucario-EX", "MEGA", "EX", "MLucarioEX"],
    subtypes=["MEGA", "EX"],
    collector_number=55,
    set_code="XY3",
    rarity=Rarities.RareHolo,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LucarioEX.Name",
    family_id=448,
    abilities=[
        Attack(
            title="Rising Fist",
            game_text="Discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=140,
            effect=unimplemented,
        ),
    ],
)