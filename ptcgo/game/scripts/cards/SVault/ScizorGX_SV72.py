from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import protect_next_turn

card = PokemonCardDef(
    guid="26f1c7b3-6bbd-5cef-a394-1e76396bfc2d",
    key="SVault",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ScizorGX.Name",
    display_name="Scizor-GX",
    searchable_by=["Scizor-GX", "Stage 1", "GX", "ScizorGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=72,
    set_code="SVault",
    rarity=Rarities.Rare,
    hp=210,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name",
    family_id=123,
    abilities=[
        Ability(
            title="Danger Perception",
            game_text="If this Pok\u00e9mon's remaining HP is 100 or less, its attacks do 80 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Steel Wing",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=protect_next_turn(reduce=30),
        ),
        Attack(
            title="Cross-Cut-GX",
            game_text="If your opponent's Active Pok\u00e9mon is an Evolution Pok\u00e9mon, this attack does 100 more damage. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)