from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack, flip_damage
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="8594e067-20ec-5692-9415-73f6f5fe8b6a",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    display_name="Nuzleaf",
    searchable_by=["Nuzleaf", "Stage 1", "Nuzleaf"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seedot.Name",
    family_id=273,
    abilities=[
        Attack(
            title="Eerie Light",
            game_text="The Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="One-Two Strike",
            game_text="Flip 2 coins. This attack does 30 damage plus 20 more damage for each heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=flip_damage(coins=2, base=30, bonus_per_heads=20),
        ),
    ],
)