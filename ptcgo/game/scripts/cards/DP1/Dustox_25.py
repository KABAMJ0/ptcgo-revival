from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="43ce42b7-7d5a-5e37-b193-be95e0230a24",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dustox.Name",
    display_name="Dustox",
    searchable_by=["Dustox", "Stage 2", "Dustox"],
    subtypes=["Stage 2"],
    collector_number=25,
    set_code="DP1",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cascoon.Name",
    family_id=265,
    abilities=[
        Attack(
            title="Stun Spore",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Toxic Dust",
            game_text="The Defending Pok\u00e9mon is now Poisoned. Put 2 damage counters instead of 1 on the Defending Pok\u00e9mon between turns.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=unimplemented,
        ),
    ],
)