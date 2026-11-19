from ptcgo.game.card_effects.attacks_common import damage_per, count_energy
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c151bdcb-2681-51b4-9e73-9cbea0d00916",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GumshoosGX.Name",
    display_name="Gumshoos-GX",
    searchable_by=["Gumshoos-GX", "Stage 1", "GX", "GumshoosGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=157,
    set_code="SM1",
    rarity=Rarities.RareRainbow,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yungoos.Name",
    family_id=734,
    abilities=[
        Ability(
            title="Search the Premises",
            game_text="Once during your turn (before your attack), you may have your opponent reveal their hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Headbutt Bounce",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
        Attack(
            title="Gumshoe Chance-GX",
            game_text="This attack does 50 damage times the amount of Energy attached to your opponent's Active Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_energy("defender"), 50),
        ),
    ],
)