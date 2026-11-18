from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5c1671c0-31ce-5bd9-99b5-1df2516d4078",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alakazamex.Name",
    display_name="Alakazam ex",
    searchable_by=["Alakazam ex", "Stage 2", "ex", "Alakazamex"],
    subtypes=["Stage 2", "ex"],
    collector_number=215,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=310,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kadabra.Name",
    family_id=63,
    abilities=[
        Attack(
            title="Mind Jack",
            game_text="This attack does 30 more damage for each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Dimensional Hand",
            game_text="This attack can be used even if this Pok\u00e9mon is on the Bench.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)