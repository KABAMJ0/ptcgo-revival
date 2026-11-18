from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_attack

card = PokemonCardDef(
    guid="5c1f946a-7f3c-5d43-a111-fee10fb802cb",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rabsca.Name",
    display_name="Rabsca",
    searchable_by=["Rabsca", "Stage 1", "Rabsca"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rellor.Name",
    family_id=953,
    abilities=[
        Attack(
            title="Triple Draw",
            game_text="Draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draw_attack(3),
        ),
        Attack(
            title="Counterturn",
            game_text="If there are 3 or fewer cards in your deck, this attack does 200 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)