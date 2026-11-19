from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.trainers import all_of, basic_energy_of, is_energy_card, named
from ptcgo.game.session.effects import is_pokemon_card, is_supporter_card
from ptcgo.game.card_effects.attacks_common import mill_scaled_damage
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d4a3a1f0-636c-5241-a80d-7a4cad0cc377",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysGyarados.Name",
    display_name="Misty's Gyarados",
    searchable_by=["Misty's Gyarados", "Stage 1", "MistysGyarados"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MistysMagikarp.Name",
    family_id=129,
    abilities=[
        Attack(
            title="Splashing Panic",
            game_text="Discard the top 7 cards of your deck, and this attack does 70 damage for each Misty's Pok\u00e9mon that you discarded in this way.",
            cost={PokemonTypes.WATER: 1},
            damage=70,
            damage_operator="x",
            effect=mill_scaled_damage(7, 70, pred=all_of(is_pokemon_card, named("misty's"))),
        ),
        Attack(
            title="Waterfall",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)