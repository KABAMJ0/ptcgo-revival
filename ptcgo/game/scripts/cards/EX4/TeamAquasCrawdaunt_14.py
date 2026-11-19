from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="85640b12-ef3d-580d-90cd-bbf3ff977594",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasCrawdaunt.Name",
    display_name="Team Aqua's Crawdaunt",
    searchable_by=["Team Aqua's Crawdaunt", "Stage 1", "TeamAquasCrawdaunt"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="EX4",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasCorphish.Name",
    family_id=341,
    abilities=[
        Attack(
            title="Poison Reaction",
            game_text="If the Defending Pok\u00e9mon is Poisoned, this attack does 20 damage plus 20 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Double Claw",
            game_text="Flip 2 coins. This attack does 30 damage plus 20 more damage for each heads.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=flip_damage(coins=2, per_heads=20, base=30),
        ),
    ],
)