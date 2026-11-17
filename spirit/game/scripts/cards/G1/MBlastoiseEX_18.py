from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6b301604-89ed-5385-971c-9bc18bbb8eff",
    key="G1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MBlastoiseEX.Name",
    display_name="M Blastoise-EX",
    searchable_by=["M Blastoise-EX", "MEGA", "EX", "MBlastoiseEX"],
    subtypes=["MEGA", "EX"],
    collector_number=18,
    set_code="G1",
    rarity=Rarities.RareHolo,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BlastoiseEX.Name",
    family_id=9,
    abilities=[
        Attack(
            title="Dread Launcher",
            game_text="Flip a coin. If tails, discard 2 Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=180,
            effect=unimplemented,
        ),
    ],
)