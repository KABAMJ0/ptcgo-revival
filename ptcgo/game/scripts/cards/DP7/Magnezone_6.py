from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ef59c08a-af60-5081-ba9f-0f69b272e837",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnezone.Name",
    display_name="Magnezone",
    searchable_by=["Magnezone", "Stage 2", "Magnezone"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="DP7",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    family_id=81,
    abilities=[
        Ability(
            title="Super Connectivity",
            game_text="Once during your turn (before your attack), you may search your discard pile for a Lightning or Metal Energy card and attach it to your Active Pok\u00e9mon. Then, put 1 damage counter on that Pok\u00e9mon. This power can't be used if Magnezone is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Gyro Ball",
            game_text="You may switch Magnezone with 1 of your Benched Pok\u00e9mon. If you do, your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
    ],
)