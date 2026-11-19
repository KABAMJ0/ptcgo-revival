from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_retreat_attack

card = PokemonCardDef(
    guid="c94741f7-ff01-5d7f-ac38-5b4c7edc22cc",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndstoneex.Name",
    display_name="Houndstone ex",
    searchable_by=["Houndstone ex", "Stage 1", "ex", "Houndstoneex"],
    subtypes=["Stage 1", "ex"],
    collector_number=102,
    set_code="SV3",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Greavard.Name",
    family_id=971,
    abilities=[
        Attack(
            title="Big Bite",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=no_retreat_attack(),
        ),
        Attack(
            title="Last Respects",
            game_text="This attack does 10 more damage for each Psychic Pok\u00e9mon in your discard pile.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)