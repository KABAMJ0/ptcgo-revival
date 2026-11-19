from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.card_effects.attacks_common import mill_attack
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="4f3c8294-3ab1-500a-84b9-ecc2e1e5490b",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gurdurr.Name",
    display_name="Gurdurr",
    searchable_by=["Gurdurr", "Stage 1", "Gurdurr"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="ZSV10PT5",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Timburr.Name",
    family_id=532,
    abilities=[
        Attack(
            title="Low Kick",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
        ),
        Attack(
            title="Hammer Arm",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=mill_attack(1),
        ),
    ],
)