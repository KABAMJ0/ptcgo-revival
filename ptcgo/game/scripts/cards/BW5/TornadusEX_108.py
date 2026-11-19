from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if, stadium_in_play_cond

card = PokemonCardDef(
    guid="a37651ba-321f-57b7-85dc-f88842e59a4f",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TornadusEX.Name",
    display_name="Tornadus-EX",
    searchable_by=["Tornadus-EX", "Basic", "EX", "TornadusEX"],
    subtypes=["Basic", "EX"],
    collector_number=108,
    set_code="BW5",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=641,
    abilities=[
        Attack(
            title="Blow Through",
            game_text="If there is any Stadium card in play, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=bonus_if(stadium_in_play_cond, 30),
        ),
        Attack(
            title="Power Blast",
            game_text="Flip a coin. If tails, discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=unimplemented,
        ),
    ],
)