from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand

card = PokemonCardDef(
    guid="caa2cb8e-1217-53db-b92c-40272279c326",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Talonflameex.Name",
    display_name="Talonflame ex",
    searchable_by=["Talonflame ex", "Stage 2", "ex", "Talonflameex"],
    subtypes=["Stage 2", "ex"],
    collector_number=124,
    set_code="ME6",
    rarity=Rarities.Rare,
    hp=280,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name",
    family_id=661,
    abilities=[
        Ability(
            title="Excited Dive",
            game_text="Once during your turn, if this Pok\u00e9mon is in your hand, and if you have any Colorless Mega Evolution Pok\u00e9mon ex in play, you may use this Ability. Put this Pok\u00e9mon onto your Bench.",
            effect=unimplemented,
        ),
        Attack(
            title="Talon Hunt",
            game_text="You may search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=search_to_hand(None, count=2, reveal=False),
        ),
    ],
)