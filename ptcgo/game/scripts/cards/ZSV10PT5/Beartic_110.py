from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="1c1c2689-3ae1-5e32-8137-eeb84049d771",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beartic.Name",
    display_name="Beartic",
    searchable_by=["Beartic", "Stage 1", "Beartic"],
    subtypes=["Stage 1"],
    collector_number=110,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cubchoo.Name",
    family_id=613,
    abilities=[
        Attack(
            title="Continuous Headbutt",
            game_text="Flip a coin until you get tails. This attack does 50 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=flip_damage(per_heads=50, until_tails=True),
        ),
        Attack(
            title="Sheer Cold",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't use attacks.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=unimplemented,
        ),
    ],
)