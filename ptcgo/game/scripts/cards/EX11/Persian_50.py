from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.attacks_common import snipe_attack
card = PokemonCardDef(
    guid="af55acd7-f2a1-5c3a-971b-8e7470cd63c9",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Persian.Name",
    display_name="Persian",
    searchable_by=["Persian", "Stage 1", "Persian"],
    subtypes=["Stage 1"],
    collector_number=50,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    family_id=52,
    abilities=[
        Ability(
            title="Prowl",
            game_text="Once during your turn, when you play Persian from your hand to evolve 1 of your Pok\u00e9mon, you may search your deck for any 1 card and put it into your hand. Shuffle your deck afterward.",
            effect=unimplemented,
        ),
        Attack(
            title="Snap Tail",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 30 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=snipe_attack(30, pool="any"),
        ),
    ],
)