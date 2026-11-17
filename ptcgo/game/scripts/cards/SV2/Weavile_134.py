from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c9b728fe-96c3-5bfd-ac15-6a6e7de13da8",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weavile.Name",
    display_name="Weavile",
    searchable_by=["Weavile", "Stage 1", "Weavile"],
    subtypes=["Stage 1"],
    collector_number=134,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    family_id=215,
    abilities=[
        Ability(
            title="Assaulting Hunt",
            game_text="Once during your turn, when this Pok\u00e9mon moves from your Bench to the Active Spot, you may switch in 1 of your opponent's Benched Basic Pok\u00e9mon to the Active Spot.",
            effect=unimplemented,
        ),
        Attack(
            title="Slashing Claw",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)