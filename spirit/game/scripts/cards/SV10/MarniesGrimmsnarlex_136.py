from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f4bfdd15-0b45-5617-8a88-e849b7a6e0a9",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MarniesGrimmsnarlex.Name",
    display_name="Marnie's Grimmsnarl ex",
    searchable_by=["Marnie's Grimmsnarl ex", "Stage 2", "ex", "MarniesGrimmsnarlex"],
    subtypes=["Stage 2", "ex"],
    collector_number=136,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=320,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MarniesMorgrem.Name",
    family_id=859,
    abilities=[
        Ability(
            title="Punk Up",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may search your deck for up to 5 Basic Darkness Energy cards and attach them to your Marnie's Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Shadow Bullet",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 2},
            damage=180,
            effect=unimplemented,
        ),
    ],
)