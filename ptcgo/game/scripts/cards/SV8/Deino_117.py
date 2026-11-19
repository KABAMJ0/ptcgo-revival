from ptcgo.game.card_effects.attacks_common import mill_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bd40702a-b80f-59f6-9a63-dfde7b41171a",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deino.Name",
    display_name="Deino",
    searchable_by=["Deino", "Basic", "Deino"],
    subtypes=["Basic"],
    collector_number=117,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=633,
    abilities=[
        Attack(
            title="Stomp Off",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=mill_attack(1, opponent=True),
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)