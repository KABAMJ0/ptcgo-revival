from ptcgo.game.card_effects.attacks_common import mill_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import mill_attack

card = PokemonCardDef(
    guid="7713fdce-e86e-5bac-854e-3789f1c3e606",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garganacl.Name",
    display_name="Garganacl",
    searchable_by=["Garganacl", "Stage 2", "Garganacl"],
    subtypes=["Stage 2"],
    collector_number=123,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Naclstack.Name",
    family_id=932,
    abilities=[
        Ability(
            title="Blessed Salt",
            game_text="During Pok\u00e9mon Checkup, heal 20 damage from each of your Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Knocking Hammer",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=130,
            effect=mill_attack(1),
        ),
    ],
)