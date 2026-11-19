from ptcgo.game.card_effects.attacks_common import mill_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a4486130-00c2-5a63-9bd6-fcf1203fbdf6",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanClodsire.Name",
    display_name="Paldean Clodsire",
    searchable_by=["Paldean Clodsire", "Stage 1", "PaldeanClodsire"],
    subtypes=["Stage 1"],
    collector_number=128,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanWooper.Name",
    family_id=194,
    abilities=[
        Attack(
            title="Poison Ring",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. During your opponent's next turn, that Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Muddy Hammer",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=mill_attack(1),
        ),
    ],
)