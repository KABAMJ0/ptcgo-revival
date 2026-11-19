from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import is_pokemon_card
from ptcgo.game.card_effects.support_common import search_to_hand

card = PokemonCardDef(
    guid="0a10b79b-a809-506d-b91d-f740693ec621",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AmpharosGX.Name",
    display_name="Ampharos-GX",
    searchable_by=["Ampharos-GX", "Stage 2", "GX", "AmpharosGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=43,
    set_code="SM9",
    rarity=Rarities.RareHolo,
    hp=240,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    family_id=179,
    abilities=[
        Attack(
            title="Power Recharge",
            game_text="Put all Electropower cards from your discard pile into your hand.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Impact Bolt",
            game_text="Discard all Lightning Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=150,
            effect=self_energy_discard_attack(all_energy=True, energy_type=PokemonTypes.LIGHTNING),
        ),
        Attack(
            title="Electrical-GX",
            game_text="Search your deck for up to 7 Pok\u00e9mon, reveal them, and put them into your hand. Then, shuffle your deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=search_to_hand(is_pokemon_card, count=7, minimum=0, reveal=True),
        ),
    ],
)