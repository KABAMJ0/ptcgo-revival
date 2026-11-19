from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.session.effects import is_item_card


card = PokemonCardDef(
    guid="08da1251-3bc6-5e43-988b-ed8df27f71d2",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    display_name="Magneton",
    searchable_by=["Magneton", "Stage 1", "Magneton"],
    subtypes=["Stage 1"],
    collector_number=82,
    set_code="SV3PT5",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    family_id=81,
    abilities=[
        Attack(
            title="Junk Magnet",
            game_text="Put up to 2 Item cards from your discard pile into your hand.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=recover_from_discard(is_item_card, count=2, to='hand'),
        ),
        Attack(
            title="Head Bolt",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)