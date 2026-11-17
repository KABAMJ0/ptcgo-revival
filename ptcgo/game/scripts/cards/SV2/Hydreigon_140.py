from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="480c3576-6b95-585f-92e6-531b447eedab",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hydreigon.Name",
    display_name="Hydreigon",
    searchable_by=["Hydreigon", "Stage 2", "Hydreigon"],
    subtypes=["Stage 2"],
    collector_number=140,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    family_id=633,
    abilities=[
        Ability(
            title="Tri Howl",
            game_text="Once during your turn, you may look at the top 3 cards of your deck and attach any number of Energy cards you find there to your Pok\u00e9mon in any way you like. Discard the other cards.",
            effect=unimplemented,
        ),
        Attack(
            title="Dark Cutter",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
        ),
    ],
)