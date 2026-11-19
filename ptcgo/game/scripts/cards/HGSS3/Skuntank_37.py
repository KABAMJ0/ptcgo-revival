from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="76811a1d-f2ab-59e0-aa38-9ac1908b59c3",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skuntank.Name",
    display_name="Skuntank",
    searchable_by=["Skuntank", "Stage 1", "Skuntank"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="HGSS3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Stunky.Name",
    family_id=434,
    abilities=[
        Attack(
            title="Stun Gas",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned. If tails, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Fury Swipes",
            game_text="Flip 3 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=30),
        ),
    ],
)