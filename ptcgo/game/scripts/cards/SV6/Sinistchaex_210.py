from ptcgo.game.card_effects.support_common import heal_targets
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.support_common import heal_targets
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import heal_targets

card = PokemonCardDef(
    guid="e3c3719c-9827-5587-bc18-6abcdf67e6a8",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sinistchaex.Name",
    display_name="Sinistcha ex",
    searchable_by=["Sinistcha ex", "Stage 1", "ex", "Sinistchaex"],
    subtypes=["Stage 1", "ex"],
    collector_number=210,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=240,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poltchageist.Name",
    abilities=[
        Attack(
            title="Re-Brew",
            game_text="Put 2 damage counters on 1 of your opponent's Pok\u00e9mon for each Basic Grass Energy card in your discard pile. Then, shuffle those Energy cards into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=heal_targets(30, scope="each_own"),
        ),
        Attack(
            title="Matcha Splash",
            game_text="Heal 30 damage from each of your Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=heal_targets(30, scope="each_own"),
        ),
    ],
)