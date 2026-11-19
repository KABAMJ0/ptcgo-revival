from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import mill_attack

card = PokemonCardDef(
    guid="e7bb83f5-e6d4-56bc-8faf-b0357bb45164",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxtricityex.Name",
    display_name="Toxtricity ex",
    searchable_by=["Toxtricity ex", "Stage 1", "Tera", "ex", "Toxtricityex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=227,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name",
    family_id=848,
    abilities=[
        Attack(
            title="Knocking Hammer",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=70,
            effect=mill_attack(1),
        ),
        Attack(
            title="Gaia Punk",
            game_text="Discard 3 Lightning Energy from your Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=270,
            effect=unimplemented,
        ),
    ],
)