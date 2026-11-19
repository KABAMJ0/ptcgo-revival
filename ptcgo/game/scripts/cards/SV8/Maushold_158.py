from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.card_effects.trainers import named

card = PokemonCardDef(
    guid="e43b03b3-9a24-5bea-a453-6919336800c8",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Maushold.Name",
    display_name="Maushold",
    searchable_by=["Maushold", "Stage 1", "Maushold"],
    subtypes=["Stage 1"],
    collector_number=158,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tandemaus.Name",
    family_id=924,
    abilities=[
        Attack(
            title="Familial March",
            game_text="Search your deck for up to 2 in any combination of Maushold and Maushold ex and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(named("maushold"), count=2),
        ),
        Attack(
            title="Incessant Incisors",
            game_text="Flip 4 coins. This attack does 30 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=4, per_heads=30),
        ),
    ],
)