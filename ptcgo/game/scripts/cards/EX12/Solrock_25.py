from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.card_effects.trainers import named_exactly
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack, flip_gate


card = PokemonCardDef(
    guid="9cef0127-3a66-5c89-bb04-3bb73065658b",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Solrock.Name",
    display_name="Solrock",
    searchable_by=["Solrock", "Basic", "Solrock"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="EX12",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=338,
    abilities=[
        Ability(
            title="Luna Shade",
            game_text="As long as you have Lunatone in play, each player's Colorless Pok\u00e9mon (excluding Pok\u00e9mon-ex) can't use any Pok\u00e9-Powers.",
            effect=unimplemented,
        ),
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Lunatone and put it onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(named_exactly("lunatone"), count=1),
        ),
        Attack(
            title="Hyper Beam",
            game_text="Flip a coin. If heads, discard an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=flip_gate(discard_opponent_energy_attack(1)),
        ),
    ],
)