from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.effects import is_pokemon_card
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.attacks_common import damage_per, count_bench
card = PokemonCardDef(
    guid="d1dfb516-cdc6-5691-9c39-9a2e9078bc4a",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuKokoex.Name",
    display_name="Tapu Koko ex",
    searchable_by=["Tapu Koko ex", "Basic", "ex", "TapuKokoex"],
    subtypes=["Basic", "ex"],
    collector_number=51,
    set_code="SV9",
    rarity=Rarities.Rare,
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=785,
    abilities=[
        Attack(
            title="Linked Lightning",
            game_text="This attack does 20 more damage for each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=damage_per(count_bench("mine"), 20, base=60),
        ),
    ],
)