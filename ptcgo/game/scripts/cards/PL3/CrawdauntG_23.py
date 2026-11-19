from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack
from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0974762d-09f9-5aa3-9fe6-abc8ca26a33f",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CrawdauntG.Name",
    display_name="Crawdaunt G",
    searchable_by=["Crawdaunt G", "Basic", "SP", "CrawdauntG"],
    subtypes=["Basic", "SP"],
    collector_number=23,
    set_code="PL3",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=342,
    abilities=[
        Attack(
            title="Smash Turn",
            game_text="You may switch Crawdaunt G with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=flip_gate(discard_opponent_energy_attack(1)),
        ),
        Attack(
            title="Hyper Beam",
            game_text="Flip a coin. If heads, discard an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=unimplemented,
        ),
    ],
)