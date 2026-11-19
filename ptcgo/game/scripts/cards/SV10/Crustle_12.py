from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="14d06db4-8ba0-5436-907a-21f6fb2d2a8f",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crustle.Name",
    display_name="Crustle",
    searchable_by=["Crustle", "Stage 1", "Crustle"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dwebble.Name",
    family_id=557,
    abilities=[
        Ability(
            title="Mysterious Rock Inn",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon ex.",
            effect=unimplemented,
        ),
        Attack(
            title="Superb Scissors",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=ignore_modifier_attack(ignore_target_effects=True),
        ),
    ],
)