from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand

card = PokemonCardDef(
    guid="3f1970b8-c1a9-517a-aa3c-1d40e90c9bdb",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MetagrossGX.Name",
    display_name="Metagross-GX",
    searchable_by=["Metagross-GX", "Stage 2", "GX", "MetagrossGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=157,
    set_code="SM2",
    rarity=Rarities.RareRainbow,
    hp=250,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    family_id=374,
    abilities=[
        Ability(
            title="Geotech System",
            game_text="Once during your turn (before your attack), you may attach a Psychic or Metal Energy card from your discard pile to your Active Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Giga Hammer",
            game_text="This Pok\u00e9mon can't use Giga Hammer during your next turn.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=unimplemented,
        ),
        Attack(
            title="Algorithm-GX",
            game_text="Search your deck for up to 5 cards and put them into your hand. Then, shuffle your deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(None, count=5, minimum=0, reveal=False),
        ),
    ],
)