from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="25acf927-d47e-5796-a808-af034197be43",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxicroakex.Name",
    display_name="Toxicroak ex",
    searchable_by=["Toxicroak ex", "Stage 1", "ex", "Toxicroakex"],
    subtypes=["Stage 1", "ex"],
    collector_number=131,
    set_code="SV1",
    rarity=Rarities.Rare,
    hp=250,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name",
    family_id=453,
    abilities=[
        Attack(
            title="Nasty Plot",
            game_text="Search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=search_to_hand(None, count=2, reveal=False),
        ),
        Attack(
            title="Toxic Ripper",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. During Pok\u00e9mon Checkup, put 6 damage counters on that Pok\u00e9mon instead of 1.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=condition_attack(SpecialConditions.POISONED, counters=6),
        ),
    ],
)