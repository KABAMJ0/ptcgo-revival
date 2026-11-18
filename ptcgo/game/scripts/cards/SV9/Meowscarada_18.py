from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="61b9d063-e7a9-5354-8913-322b7c57891a",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowscarada.Name",
    display_name="Meowscarada",
    searchable_by=["Meowscarada", "Stage 2", "Meowscarada"],
    subtypes=["Stage 2"],
    collector_number=18,
    set_code="SV9",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Floragato.Name",
    family_id=906,
    abilities=[
        Ability(
            title="Showtime",
            game_text="Once during your turn, if this Pok\u00e9mon is on your Bench, you may switch it with your Active Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Rising Bloom",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon ex, this attack does 90 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)